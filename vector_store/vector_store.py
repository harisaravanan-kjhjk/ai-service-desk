import chromadb

client = chromadb.PersistentClient(path="./ticket_vectors")

ticket_collection = client.get_or_create_collection(
    name="resolved_tickets"
)

resolution_collection=client.get_or_create_collection(
    name="resolved_notes"
)