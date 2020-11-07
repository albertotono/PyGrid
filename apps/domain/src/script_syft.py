from typing import List
from typing import Tuple

import torch as th

from syft.core.common import UID
from syft.core.store.storeable_object import StorableObject

def generate_id_obj(
    data: th.Tensor, description: str, tags: List[str]
) -> Tuple[UID, StorableObject]:
    _id = UID()
    obj = StorableObject(id=_id, data=data, description=description, tags=tags)

    return _id, obj


id1, obj1 = generate_id_obj(
    data=th.Tensor([1, 2, 3, 4]),
    description="Dummy tensor",
    tags=["dummy", "tensor"],
)


