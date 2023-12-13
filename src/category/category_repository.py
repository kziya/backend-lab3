from src import db
from src.category.category_model import CategoryModel


class CategoryRepository:
    _categories = []

    def addCategory(self, name):
        category = CategoryModel(name=name)
        db.session.add(category)
        db.session.commit()

        return category.toDict()

    def removeCategoryById(self, id):
        categoryToDelete = CategoryModel.query.get(id)
        if categoryToDelete is not None:
            db.session.delete(categoryToDelete)
            db.session.commit()

        return True

    def getAllCategories(self):
        return CategoryModel.toDictList(CategoryModel.query.all())

    def getCategoryById(self, id):
        category = CategoryModel.query.get(id)
        if category is not None:
            return category.toDict()
        else:
            return None


categoryRepository = CategoryRepository()
