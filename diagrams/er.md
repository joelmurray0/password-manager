```mermaid
erDiagram
    USER {
     string userName
    }

    USER_ACCOUNT {
     string username
     string master_password
    }

    ENCRYPTED_PASSWORD {
     string encryptedUsername
     string encryptedPassword
     string url
     string password_key
    }

     DATABASE{
     list~string~ ENCRYPTED_PASSWORD
     }

    USER ||--o{ USER_ACCOUNT : owns
    DATABASE ||--o{ ENCRYPTED_PASSWORD : stores
    USER_ACCOUNT ||--|| DATABASE : has
