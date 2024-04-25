from typing import TypeAlias
ItemPrices: TypeAlias = list[tuple[str, float]]

from typing import TypeVar

from dataclasses import dataclass

TOrganization = TypeVar("Self", bound = "Organization")

@dataclass(frozen=True)
class Organization:
    name: str
    parent: TOrganization | None
    

org1 = Organization("Product Division", None)
org2 = Organization("Platform Team", org1)
org3 = Organization("Algorithm unit", org2)

print(f"{org3.name=}{org3.parent.name}{org3.parent.parent.name=}")