from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from ..core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
router = APIRouter(tags=["Protected"])

def get_role(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("role")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@router.get("/protected")
def protected(role: str = Depends(get_role)):
    return {"msg": f"Access granted as {role}"}

@router.get("/admin")
def admin(role: str = Depends(get_role)):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return {"msg": "Welcome admin"}