```mermaid
classDiagram
    class Users {
        - userAccounts : List~UserAccount~
        + addUserAccount(account: UserAccount) : void
        + removeUserAccount(account: UserAccount) : void
        
    }

    class UserAccount {
        - username : String
        - password : EncryptedPassword
        - passwordStrength : String
        + changePassword(newPassword: String) : void
        + checkPasswordStrength(password: String) : String
        + encryptPassword(password: String) : String
        + decryptPassword(encryptedPassword: String) : String
    }

    class EncryptedPassword {
        - encryptedData : String
        - encryptionMethod : String
        
    }

    class PasswordGenerator {
        + generateStrongPassword(length: int) : String
    }

    class PasswordChecker {
        + checkPassword(password: String) : bool
    }

    class EncryptionMethod {
        + encrypt(password: String) : String
        + decrypt() : String
    }

    Users "1" --> "0..*" UserAccount 
    UserAccount "1" *-- "0..*" EncryptedPassword 
    UserAccount "1" *-- "1" PasswordGenerator
    UserAccount "1" o-- "1" PasswordChecker
    UserAccount "1" *-- "1" EncryptionMethod 
