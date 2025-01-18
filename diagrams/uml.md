```mermaid
classDiagram
    class KeyManager {
        - Key : Dict~Key~
        + addKey(account: UserAccount) : void
        + removeKey(account: UserAccount) : void
        
    }

    class Key {
        - username : string
        - master_password : string
    }

    class Vault {
        - key : Key
        - items : List
        + add_item(new_item: vaultItem) : void
        + delete_item(item: vaultItem) : void
        + edit_item(item: vaultItem) : void
    }

    class vaultItem {
        - username : string
        - password : string
        - key : string
        - url : string
        + encrypt_item(master_password: Key) : void
        + decrypt_item(master_password: Key) : void
    }

    class PasswordGenerator {
        + character_requirements : list
        + generateStrongPassword(length: int) : string
    }

    class PasswordChecker {
        - vulnerablePasswords: list~string~
        + checkPassword(password: string) : bool
    }

    class Encryption {
        + encrypt(password: string) : string
        + decrypt(ciphertext: string) : string
    }

    Vault "1" *-- "1" Key
    KeyManager "1" *-- "0..*" Key
    vaultItem  "1" --> "1" PasswordChecker
    vaultItem  "1" --> "1" PasswordGenerator
    Vault "1" *-- "0..*" vaultItem
    Encryption "1" --> "1" Vault
    Encryption "1" --> "1" vaultItem
    vaultItem "1" *-- "1" Key
