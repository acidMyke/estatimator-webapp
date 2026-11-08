from sqlmodel import Session, func, select

from api_services.features.admin.models import Admin


def get_admin_by_email(db: Session, email: str) -> Admin | None:
    stmt = select(Admin).where(
        func.lower(Admin.email) == email.strip().lower(),
        Admin.deleted_at == None,
    )
    return db.exec(stmt).first()


def create_admin(db: Session, email: str, name: str) -> Admin:
    admin = Admin(email=email.strip().lower(), name=name.strip())
    db.add(admin)
    return admin
