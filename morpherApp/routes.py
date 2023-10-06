from typing import Optional

from fastapi import Body, APIRouter
from pytrovich.enums import Gender as PytrovichGender

from enums import CommonCase, HTTPCase
from morpher import morph_post, morph_fio

morph_router = APIRouter(prefix="/morph")
case_idx_body = Body(ge=1, le=6)


@morph_router.post("/post")
async def morph_post_handler(post: str = Body(),
                             case_idx: int = case_idx_body):
    return {"morphed_post": morph_post(
        post=post,
        case=CommonCase[HTTPCase[case_idx]]
    )}


@morph_router.post("/post/all")
async def morph_post_handler(post: str = Body(embed=True)):
    return {
        i: morph_post(
            post=post,
            case=case
        )
        for i, case in enumerate(CommonCase, 1)
    }


@morph_router.post("/fio")
async def morph_fio_handler(
        fio: str = Body(),
        case_idx: int = case_idx_body,
        gender: Optional[PytrovichGender] = Body(default=None),
        content_order: str = Body(default="fio")
):
    return {"morphed_fio": morph_fio(
        fio=fio,
        case=CommonCase[HTTPCase[case_idx]],
        gender=gender,
        content_order=content_order
    )}


@morph_router.post("/fio/all")
async def morph_fio_handler(
        fio: str = Body(),
        gender: Optional[PytrovichGender] = Body(default=None),
        content_order: str = Body(default="fio")
):
    return {
        i: morph_fio(
            fio=fio,
            case=case,
            gender=gender,
            content_order=content_order
        )
        for i, case in enumerate(CommonCase, 1)}
