import time
import pytest
from Guia2.queu import Queue

# --- INTEGRACION AL DOMINIO ---
def run_benchmark():
    for size in [1000, 10000, 100000]:
        q = Queue[int]()
        t0 = time.time()
        for i in range(size): q.enqueue(i)
        t_enq = time.time() - t0
        
        t0 = time.time()
        for _ in range(size): q.dequeue()
        t_deq = time.time() - t0
        
        print(f"Size: {size:<6} | Enqueue: {t_enq:.4f}s | Dequeue: {t_deq:.4f}s")

# --- PRUEBAS UNITARIAS--
def test_queue_operations():
    q = Queue[str]()
    assert q.is_empty() is True                                    # Estructura vacía
    q.enqueue("Paracetamol")
    assert q.size() == 1                                           # Inserción
    assert q.search("Paracetamol") is True                         # Búsqueda exitosa
    assert q.search("Ibuprofeno") is False                         # Búsqueda fallida
    assert q.dequeue() == "Paracetamol"                            # Eliminación
    assert q.is_empty() is True