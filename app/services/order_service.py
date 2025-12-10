from typing import List, Optional

from sqlalchemy.orm import Session

from app.models import Order
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.user_repository import UserRepository
from app.schemas import OrderCreate


class OrderService:
    def __init__(
        self,
        order_repository: OrderRepository,
        product_repository: ProductRepository,
        user_repository: UserRepository,
    ) -> None:
        self.order_repository = order_repository
        self.product_repository = product_repository
        self.user_repository = user_repository

    async def create_order(self, session: Session, order_data: OrderCreate) -> Order:
        user = await self.user_repository.get_by_id(session, order_data.user_id)
        if not user:
            raise ValueError("User not found")

        if not order_data.items:
            raise ValueError("Order items cannot be empty")

        return await self.order_repository.create(session, order_data)

    async def get_order(self, session: Session, order_id: int) -> Optional[Order]:
        return await self.order_repository.get(session, order_id)

    async def list_orders(
        self,
        session: Session,
        count: int = 10,
        page: int = 1,
        user_id: Optional[int] = None,
    ) -> List[Order]:
        return await self.order_repository.list(
            session, count=count, page=page, user_id=user_id
        )

    async def update_status(
        self, session: Session, order_id: int, status: str
    ) -> Optional[Order]:
        return await self.order_repository.update_status(session, order_id, status)

    async def delete_order(self, session: Session, order_id: int) -> bool:
        return await self.order_repository.delete(session, order_id)
