# GraphQL Schema для клиентского API

```graphql
"""
Тип, представляющий клиента с его основной информацией
"""
type Client {
  id: ID!
  name: String!
  age: Int!
  documents: [Document!]!
  relatives: [Relative!]!
}

"""
Тип, представляющий документ клиента
"""
type Document {
  id: ID!
  type: DocumentType!
  number: String!
  issueDate: String!
  expiryDate: String!
}

"""
Тип, представляющий родственника клиента
"""
type Relative {
  id: ID!
  relationType: RelationType!
  name: String!
  age: Int!
}

"""
Перечисление типов документов
"""
enum DocumentType {
  PASSPORT
  DRIVER_LICENSE
  TAX_ID
  SNILS
  BIRTH_CERTIFICATE
  OTHER
}

"""
Перечисление типов родственных связей
"""
enum RelationType {
  SPOUSE
  CHILD
  PARENT
  SIBLING
  OTHER
}

"""
Входной объект для фильтрации документов
"""
input DocumentFilter {
  type: DocumentType
  issueDateFrom: String
  issueDateTo: String
}

"""
Входной объект для фильтрации родственников
"""
input RelativeFilter {
  relationType: RelationType
  ageFrom: Int
  ageTo: Int
}

"""
Корневой тип Query - все точки входа в API
"""
type Query {
  """
  Получить клиента по ID с возможностью выбора вложенных данных
  """
  client(id: ID!): Client!
  
  """
  Получить документы клиента с возможностью фильтрации
  """
  documents(clientId: ID!, filter: DocumentFilter): [Document!]!
  
  """
  Получить родственников клиента с возможностью фильтрации
  """
  relatives(clientId: ID!, filter: RelativeFilter): [Relative!]!
  
  """
  Получить клиента с документами и родственниками в одном запросе
  """
  clientFull(id: ID!): Client!
}

"""
Тип для мутаций (изменения данных)
"""
type Mutation {
  """
  Обновить информацию о клиенте
  """
  updateClient(id: ID!, input: ClientInput!): Client!
  
  """
  Добавить документ клиенту
  """
  addDocument(clientId: ID!, document: DocumentInput!): Document!
  
  """
  Удалить документ клиента
  """
  removeDocument(id: ID!): Boolean!
  
  """
  Добавить родственника клиенту
  """
  addRelative(clientId: ID!, relative: RelativeInput!): Relative!
  
  """
  Удалить родственника клиента
  """
  removeRelative(id: ID!): Boolean!
}

"""
Входной объект для создания/обновления клиента
"""
input ClientInput {
  name: String
  age: Int
}

"""
Входной объект для создания документа
"""
input DocumentInput {
  type: DocumentType!
  number: String!
  issueDate: String!
  expiryDate: String!
}

"""
Входной объект для создания родственника
"""
input RelativeInput {
  relationType: RelationType!
  name: String!
  age: Int!
}
```


## Основные типы

### Client
Тип, представляющий клиента с его основной информацией.

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | `ID!` | Уникальный идентификатор клиента |
| `name` | `String!` | Имя клиента |
| `age` | `Int!` | Возраст клиента |
| `documents` | `[Document!]!` | Список документов клиента |
| `relatives` | `[Relative!]!` | Список родственников клиента |

### Document
Тип, представляющий документ клиента.

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | `ID!` | Уникальный идентификатор документа |
| `type` | `DocumentType!` | Тип документа |
| `number` | `String!` | Номер документа |
| `issueDate` | `String!` | Дата выдачи документа |
| `expiryDate` | `String!` | Дата окончания срока действия |

### Relative
Тип, представляющий родственника клиента.

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | `ID!` | Уникальный идентификатор родственника |
| `relationType` | `RelationType!` | Тип родственной связи |
| `name` | `String!` | Имя родственника |
| `age` | `Int!` | Возраст родственника |

---

## Перечисления (Enums)

### DocumentType
Перечисление типов документов.

| Значение | Описание |
|----------|----------|
| `PASSPORT` | Паспорт |
| `DRIVER_LICENSE` | Водительское удостоверение |
| `TAX_ID` | ИНН |
| `SNILS` | СНИЛС |
| `BIRTH_CERTIFICATE` | Свидетельство о рождении |
| `OTHER` | Иной документ |

### RelationType
Перечисление типов родственных связей.

| Значение | Описание |
|----------|----------|
| `SPOUSE` | Супруг/супруга |
| `CHILD` | Ребёнок |
| `PARENT` | Родитель |
| `SIBLING` | Брат/сестра |
| `OTHER` | Иная связь |

---

## Входные объекты (Inputs)

### DocumentFilter
Входной объект для фильтрации документов.

| Поле | Тип | Описание |
|------|-----|----------|
| `type` | `DocumentType` | Фильтр по типу документа |
| `issueDateFrom` | `String` | Дата выдачи: начальная граница диапазона |
| `issueDateTo` | `String` | Дата выдачи: конечная граница диапазона |

### RelativeFilter
Входной объект для фильтрации родственников.

| Поле | Тип | Описание |
|------|-----|----------|
| `relationType` | `RelationType` | Фильтр по типу родственной связи |
| `ageFrom` | `Int` | Возраст: нижняя граница |
| `ageTo` | `Int` | Возраст: верхняя граница |

### ClientInput
Входной объект для создания/обновления клиента.

| Поле | Тип | Описание |
|------|-----|----------|
| `name` | `String` | Новое имя клиента |
| `age` | `Int` | Новый возраст клиента |

### DocumentInput
Входной объект для создания документа.

| Поле | Тип | Обязательное | Описание |
|------|-----|:-----------:|----------|
| `type` | `DocumentType!` | ✅ | Тип документа |
| `number` | `String!` | ✅ | Номер документа |
| `issueDate` | `String!` | ✅ | Дата выдачи |
| `expiryDate` | `String!` | ✅ | Срок действия |

### RelativeInput
Входной объект для создания родственника.

| Поле | Тип | Обязательное | Описание |
|------|-----|:-----------:|----------|
| `relationType` | `RelationType!` | ✅ | Тип связи |
| `name` | `String!` | ✅ | Имя родственника |
| `age` | `Int!` | ✅ | Возраст родственника |

---

## Корневые типы операций

### Query
Корневой тип Query — все точки входа для получения данных.

| Запрос | Аргументы | Возвращает | Описание |
|--------|-----------|------------|----------|
| `client` | `id: ID!` | `Client!` | Получить клиента по ID с возможностью выбора вложенных данных |
| `documents` | `clientId: ID!` <br> `filter: DocumentFilter` | `[Document!]!` | Получить документы клиента с возможностью фильтрации |
| `relatives` | `clientId: ID!` <br> `filter: RelativeFilter` | `[Relative!]!` | Получить родственников клиента с возможностью фильтрации |
| `clientFull` | `id: ID!` | `Client!` | Получить клиента с документами и родственниками в одном запросе |

### Mutation
Тип для мутаций (изменения данных).

| Мутация | Аргументы | Возвращает | Описание |
|---------|-----------|------------|----------|
| `updateClient` | `id: ID!` <br> `input: ClientInput!` | `Client!` | Обновить информацию о клиенте |
| `addDocument` | `clientId: ID!` <br> `document: DocumentInput!` | `Document!` | Добавить документ клиенту |
| `removeDocument` | `id: ID!` | `Boolean!` | Удалить документ клиента |
| `addRelative` | `clientId: ID!` <br> `relative: RelativeInput!` | `Relative!` | Добавить родственника клиенту |
| `removeRelative` | `id: ID!` | `Boolean!` | Удалить родственника клиента |

---

## Примечания

- Восклицательный знак (`!`) в типах означает, что поле **обязательное** (non-nullable) — оно никогда не вернёт `null`.
- Квадратные скобки (`[ ]`) обозначают **массив** значений указанного типа.
- Для операций удаления возвращается `Boolean!` — `true` при успешном удалении, `false` в противном случае.



## Примеры GraphQL-запросов

## 1. Получение базовой информации о клиенте
Аналог REST: `GET /clients/{id}`

### Запрос
```graphql
query GetClient($id: ID!) {
  client(id: $id) {
    id
    name
    age
  }
}
Переменные
json
{
  "id": "123e4567-e89b-12d3-a456-426614174000"
}
Ответ
json
{
  "data": {
    "client": {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "name": "Иванов Иван Иванович",
      "age": 35
    }
  }
}
