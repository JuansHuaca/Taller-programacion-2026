from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from src.taller.infrastructure.orm.models import MedicineBatch

class MedicineBatchRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, batch: MedicineBatch) -> MedicineBatch:
        self.session.add(batch)
        self.session.commit()
        self.session.refresh(batch)
        return batch

    def get_by_id(self, batch_id: int) -> Optional[MedicineBatch]:
        return self.session.query(MedicineBatch).filter(MedicineBatch.id == batch_id).first()

    def update_quantity(self, batch_id: int, new_qty: int) -> Optional[MedicineBatch]:
        batch = self.get_by_id(batch_id)
        if batch:
            batch.available_quantity = new_qty
            self.session.commit()
            self.session.refresh(batch)
        return batch

    def get_all_batches_with_details(self) -> List[MedicineBatch]:
        """Solución al problema N+1 mediante joinedload"""
        return (
            self.session.query(MedicineBatch)
            .options(
                joinedload(MedicineBatch.medicine),
                joinedload(MedicineBatch.supplier)
            )
            .all()
        )