import dataclasses
import datetime

from app.order_line import OrderLine


@dataclasses.dataclass(eq=False)
class Batch:
    reference: str
    sku: str
    quantity: int
    eta: datetime.date

    def allocate(self, order_line: OrderLine):
        self.quantity -= order_line.quantity

    @property
    def available_quantity(self):
        return self.quantity
