from base import Session, Base, engine


def delete_db():
    session = Session()
    Base.metadata.reflect(bind=engine)  # To reflect any tables in the DB, but not in the current schema
    Base.metadata.drop_all(bind=engine)
    session.commit()


if __name__ == "__main__":
    delete_db()