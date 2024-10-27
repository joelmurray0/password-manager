```mermaid
classDiagram
    class Users {
        - userAccounts : List~UserAccount~
        + addUserAccount(account: UserAccount) : void
        + removeUserAccount(account: UserAccount) : void
        
    }

    class UserAccount {
        - username : string
        - password : EncryptedPassword
        - passwordStrength : string
        + changePassword(newPassword: string) : void
        + checkPasswordStrength(password: string) : string
        + encryptPassword(password: string) : string
        + decryptPassword(encryptedPassword: string) : string
    }

    class EncryptedPassword {
        - encryptedData : string
        - encryptionMethod : string
        
    }

    class PasswordGenerator {
        + generateStrongPassword(length: int) : string
    }

    class PasswordChecker {
        - vulnerablePasswords: list<string>
        + checkPassword(password: string) : bool
    }

    class EncryptionMethod {
        + encrypt(password: string) : string
        + decrypt() : string
    }

    Users "1" --> "0..*" UserAccount 
    UserAccount "1" *-- "0..*" EncryptedPassword 
    UserAccount "1" *-- "1" PasswordGenerator
    UserAccount "1" o-- "1" PasswordChecker
    UserAccount "1" *-- "1" EncryptionMethod 
