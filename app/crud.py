from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_authors(db: Session):
    return db.query(models.Author).all()


def update_author(db: Session, author_id: int, author_update: schemas.AuthorCreate):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author:
        db_author.name = author_update.name
        db_author.email = author_update.email
        db.commit()
        db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
    return db_author


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session):
    return db.query(models.Category).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def update_category(db: Session, category_id: int, category_update: schemas.CategoryCreate):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db_category.name = category_update.name
        db.commit()
        db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category


def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()


def get_tags(db: Session):
    return db.query(models.Tag).all()


def update_tag(db: Session, tag_id: int, tag_update: schemas.TagCreate):
    db_tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if db_tag:
        db_tag.name = tag_update.name
        db.commit()
        db.refresh(db_tag)
    return db_tag


def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if db_tag:
        db.delete(db_tag)
        db.commit()
    return db_tag


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(
        title=post.title,
        content=post.content,
        author_id=post.author_id,
        category_id=post.category_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    tags = []
    for tag_id in post.tags:
        tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
        if tag:
            tags.append(tag)

    db_post.tags.extend(tags)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts(db: Session):
    return db.query(models.Post).all()


def update_post(db: Session, post_id: int, post_update: schemas.PostCreate):
    db_post = db.query(models.Tag).filter(models.Tag.id == post_id).first()
    if db_post:
        db_post.title = post_update.title
        db_post.content = post_update.content
        db_post.tags = post_update.tags
        db.commit()
        db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post
