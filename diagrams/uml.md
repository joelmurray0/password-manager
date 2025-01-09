```mermaid
classDiagram
    class KeyManager {
        - Key : Dict~Key~
        + addKey(account: UserAccount) : void
        + removeKey(account: UserAccount) : void
        
    }

    class Key {
        - username : string
        - password : EncryptedPassword
        - passwordStrength : string
        + changePassword(newPassword: string) : void
        + checkPasswordStrength(password: string) : string
        + encryptPassword(password: string) : string
        + decryptPassword(encryptedPassword: string) : string
    }

    class Vault {
        - 

    class EncryptedPassword {
        - encryptedData : string
        - encryptionMethod : string
        
    }

    class PasswordGenerator {
        + generateStrongPassword(length: int) : string
    }

    class PasswordChecker {
        - vulnerablePasswords: list~string~
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
