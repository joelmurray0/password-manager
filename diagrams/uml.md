```mermaid
classDiagram
    class CLIManager {
        - spam : Spam
        + run() : void
        + create_vault() : void
        + search() : void
        + select_from_search(results: list): void
        + current_item(url: string, results: list): void
        + show_item(url: string): void
        + edit_item(url: string): void
        + remove_item(url: string): void
        + add_choice(): void
        + add(generated) : void
        + list() : void
        + home_screen() : void
        + input_with_validation(input: string, expected_results: list): string
    }

    class Spam {
        - vault : Vault
        - bloom_filter : BloomFilter
        + list_items() : list
        + remove_item(url) : void
        + get_item(url) : list
        + add_item(url) : bool
        + generate_password() : string
        + search(query) : list
        
    }

    class BloomFilter {
        - size : int
        - bit_array : list
        + _hashes(item: str) : list
        + add(item: str) : void
        + check_not_in(item: str) : bool
        + save(filename: str) : void
        + load(filename: str) : BloomFilter
    }

    class Vault {
        - master_password : string
        - items : dict
        - inverse_index : dict
        + get_vault(name, master_password) : Vault
        + _save() : void
        + _get_vault_item(url, username, password): VaultItem
        + get_item(url): VaultItem
        + add_item(new_item: vaultItem) : void
        + remove_item(url)
        + add_to_inverse_index(item, index) : void
        + remove_from_inverse_index(index) : void
        + get_items_as_list() : void
        + get_password() : string
        + get_username() : string
        + delete_item(item: vaultItem) : void
        + edit_item(item: vaultItem) : void
        + search(query) : list
        + build_search(vaultItem) : void

    }

    class vaultItem {
        - username : string
        - password : string
        - key : string
        - url : string
        + _put_(master_password, url, username, password) : void
        + get_username(master_password) : string
        + get_password(master_password) : string
        + decode_key() : string
    }

    Spam "1" *-- "1" Vault
    Vault "1" *-- "0..*" vaultItem
    Spam "1" *-- "1" BloomFilter
    Spam "1" *-- "1" CLIManager
