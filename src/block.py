def mine_block(miner_address, mempool, utxo_manager, num_txs=5):
selected_txs = mempool.get_top_transactions(num_txs)
if not selected_txs:
return None

block_fees = 0
for tx in selected_txs:
for inp in tx.inputs:
utxo_manager.remove_utxo(inp["prev_tx"], inp["index"])
for i, out in enumerate(tx.outputs):
utxo_manager.add_utxo(tx.tx_id, i, out["amount"], out["address"])

block_fees += round(tx.fee, 8)
mempool.transactions = [t for t in mempool.transactions if t.tx_id != tx.tx_id]
for inp in tx.inputs:
mempool.spent_utxos.discard((inp["prev_tx"], inp["index"]))

cb_id = f"coinbase_{uuid.uuid4().hex[:6]}"
utxo_manager.add_utxo(cb_id, 0, block_fees, miner_address)
return {"tx_count": len(selected_txs), "fees": block_fees, "miner": miner_address}
