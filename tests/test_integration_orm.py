import pytest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.taller.infrastructure.orm.models import Base, Medicine, Supplier, MedicineBatch
from src.taller.infrastructure.repositories.batch_repository import MedicineBatchRepository

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

def test_create_medicine_and_batch_integration(db_session):
    med = Medicine(barcode="7501002234510", trade_name="Ibuprofeno 400mg", active_ingredient="Ibuprofeno", laboratory="Genfar")
    supp = Supplier(company_name="Pharma Dist", tax_id="900123456", phone="3001234567")
    db_session.add_all([med, supp])
    db_session.commit()

    repo = MedicineBatchRepository(db_session)
    batch = MedicineBatch(medicine_id=med.id, supplier_id=supp.id, batch_number="LOT-2026-A", expiration_date=date(2026, 11, 15), available_quantity=100, purchase_price=4.50)
    created = repo.create(batch)

    assert created.id is not None
    assert created.batch_number == "LOT-2026-A"

def test_update_batch_stock_integration(db_session):
    med = Medicine(barcode="12345", trade_name="Paracetamol", active_ingredient="Paracetamol", laboratory="Bayer")
    supp = Supplier(company_name="Dist", tax_id="123", phone="123")
    db_session.add_all([med, supp])
    db_session.commit()

    repo = MedicineBatchRepository(db_session)
    batch = repo.create(MedicineBatch(medicine_id=med.id, supplier_id=supp.id, batch_number="B1", expiration_date=date(2027, 1, 1), available_quantity=50, purchase_price=2.0))
    
    updated = repo.update_quantity(batch.id, 30)
    assert updated.available_quantity == 30

def test_eager_loading_n_plus_one_prevention(db_session):
    med = Medicine(barcode="999", trade_name="Amoxicilina", active_ingredient="Amoxicilina", laboratory="Genfar")
    supp = Supplier(company_name="Supp", tax_id="999", phone="999")
    db_session.add_all([med, supp])
    db_session.commit()

    repo = MedicineBatchRepository(db_session)
    repo.create(MedicineBatch(medicine_id=med.id, supplier_id=supp.id, batch_number="B2", expiration_date=date(2026, 12, 1), available_quantity=20, purchase_price=5.0))

    results = repo.get_all_batches_with_details()
    assert len(results) == 1
    assert results[0].medicine.trade_name == "Amoxicilina"
    assert results[0].supplier.company_name == "Supp"