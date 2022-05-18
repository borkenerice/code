import dataclasses


@dataclasses.dataclass(eq=False)
class OrderLine:
    orderid: str
    sku: str
    quantity: int

