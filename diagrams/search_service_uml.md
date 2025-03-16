```mermaid
classDiagram
    class SearchService {
        - Key : Dict~Key~
        + addKey(account: UserAccount) : void
        + removeKey(account: UserAccount) : void
    }

    class InverseIndex {
        + add(string: string, id: int): void
        + remove(id: int): void
        + search(query: string): list
    }

    class Tokeniser {
        - key : Key
        - items : List
        + add_item(new_item: vaultItem) : void
        + delete_item(item: vaultItem) : void
        + edit_item(item: vaultItem) : void
    }

    Vault "1" *-- "1" Key
    KeyManager "1" *-- "0..*" Key
    vaultItem  "1" --> "1" PasswordChecker
    vaultItem  "1" --> "1" PasswordGenerator
    Vault "1" *-- "0..*" vaultItem
    Encryption "1" --> "1" Vault
    Encryption "1" --> "1" vaultItem
    vaultItem "1" *-- "1" Key