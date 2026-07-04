from locust import HttpUser, between, task
import random

class WebsiteUser(HttpUser):
    # Устанавливаем интервал между запросами от 0.5 до 2 секунд
    wait_time = between(0.5, 2)
    
    @task(5)
    def index(self):
        """Основной сценарий - получение ID пода"""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")
            elif len(response.text) < 5:
                response.failure("Response too short")
    
    @task(2)
    def metrics(self):
        """Сценарий получения метрик Prometheus"""
        self.client.get("/metrics")
    
    @task(1)
    def index_slow(self):
        """Сценарий с искусственной задержкой"""
        # Имитация медленного пользователя
        time.sleep(random.uniform(0.1, 0.3))
        self.client.get("/")
    
    def on_start(self):
        """Выполняется при старте каждого пользователя"""
        print(f"User started")