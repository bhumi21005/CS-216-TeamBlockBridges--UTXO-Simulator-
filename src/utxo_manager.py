
class UTXOManager:
    def _init_(self):
        self.utxo_set = {}

    def add_utxo(self, tx_id, index, amount, owner):
        self.utxo_set[(tx_id, index)] = {
            "amount": round(amount, 8), "owner": owner}

    def remove_utxo(self, tx_id, index):
        if (tx_id, index) in self.utxo_set:
            del self.utxo_set[(tx_id, index)]

    def get_balance(self, owner):
        return sum(utxo["amount"] for utxo in self.utxo_set.values() if utxo["owner"] == owner)

    def exists(self, tx_id, index):
        return (tx_id, index) in self.utxo_set

    def get_utxos_for_owner(self, owner):
        return [key for key, val in self.utxo_set.items() if val["owner"] == owner]
