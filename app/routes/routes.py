from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
from app.models.dummy import Dummy
from pydantic import BaseModel

router = APIRouter()


# validate model
class DummyCreate(BaseModel):
    test: str


# validate delete
def is_valid_id(id: str) -> bool:
    return ObjectId.is_valid(id)


@router.get("/", response_model=List[Dummy])
async def get_tests():
    tests = await Dummy.find_all().to_list()
    return tests


@router.post("/", response_model=Dummy)
async def create_test(test: DummyCreate):
    new_test = Dummy(test=test.test)
    await new_test.insert()
    return new_test


@router.delete("/{id}")
async def delete_test(id: str):
    if not is_valid_id(id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    test = await Dummy.get(id)
    if test:
        await test.delete()
        return {"message": "Dummy deleted"}
    else:
        raise HTTPException(status_code=404, detail="Dummy not found")
