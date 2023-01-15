# Querysets
---

### 1. Creating objects
#### 1.1 Create new object using class name
###### This performs an INSERT SQL statement behind the scenes. Django doesn’t hit the database until you explicitly call save().
```python
vehicle = Vehicle(make="Toyota", model="Corolla", plate_number="AP6060HT")
vehicle.save()
vehicle
<Vehicle: Toyota Corolla>
```

#### 1.2 Create new object using manager
```python
Vehicle.objects.create(make="Toyota", model="Camry", plate_number="AP6061HT")
<Vehicle: Toyota Camry>
```

#### 1.3 Set object for many to many fields
```python
vehicle1 = Vehicle.objects.create(make="Toyota", model="Camry", plate_number="AP6062HT")
driver1 = CustomUser.objects.create(
    email="driver@test.com", first_name="Test", last_name="Driver", profile_type=CustomUser.ProfileType.DRIVER
)
vehicle1.allowed_drivers.add(driver1)
vehicle1.allowed_drivers.all()
<QuerySet [<Vehicle: Toyota Camry>]>
```
```python
vehicle1 = Vehicle.objects.create(make="Toyota", model="Camry", plate_number="AP6063HT")
driver1 = CustomUser.objects.create(
    email="driver2@test.com", first_name="Test", last_name="Driver", profile_type=CustomUser.ProfileType.DRIVER
)
driver2 = CustomUser.objects.create(
    email="driver3@test.com", first_name="Test", last_name="Driver", profile_type=CustomUser.ProfileType.DRIVER
)
vehicle1.allowed_drivers.add(driver1, driver2)

# or if you have array of objects 

vehicle1.allowed_drivers.set([driver1, driver2])
```

### 2. Retrieving objects
###### To retrieve objects from your database, construct a QuerySet via a Manager on your model class.
###### Each model has at least one Manager, and it’s called "objects" by default. 
##### 2.1 Retrieving all objects
```python
Vehicle.objects.all()
<QuerySet [<Vehicle: Toyota Camry>, <Vehicle: Toyota Camry>]>
```
##### 2.2 Retrieving objects with filter or exclude
```python
Vehicle.objects.filter(year_of_production__gt=2014)
<QuerySet [<Vehicle: Toyota Camry>, <Vehicle: Toyota Camry>]>

Vehicle.objects.exclude(year_of_production__gt=2014)
<QuerySet [<Vehicle: Toyota Camry>, <Vehicle: Toyota Camry>]>

# You can use both 
Vehicle.objects.filter(year_of_production__gt=2014).exclude(make="Toyota")
<QuerySet [<Vehicle: Ford Focus>]>
```
##### 2.3 Retrieving objects with filter using Q
```python
from django.db.models import Q
# Use "or"
Vehicle.objects.filter(Q(year_of_production__gt=2000) | Q(year_of_production__lt=2018))
<QuerySet [<Vehicle: Toyota Camry>, <Vehicle: Toyota Camry>]>

# Use "or" and "and"
Vehicle.objects.filter(Q(year_of_production__gt=2000) | Q(year_of_production__lt=2018) & Q(make__contains="T"))
<QuerySet [<Vehicle: Toyota Camry>]>
```
##### 2.4 Filter by relation
```python
Book.objects.filter(authors__age__gt=50)
<QuerySet [<Book: Book: Title>]>
```
##### 2.5 Retrieving a single object with get
```python
Author.objects.get(pk=1)
<Author: qwrd kjdfv>
```
### 3. Caching and QuerySets
#### Bad way (2 query to db)
```python
print([b.title for b in Book.objects.all()])
print([b.page_count for b in Book.objects.all()])
``` 
#### Good way (1 query to db)
```python
book_queryset = Book.objects.all()
print([b.title for b in book_queryset])
print([b.page_count for b in book_queryset])
``` 
### 4. When QuerySets are not cached
```python
book_queryset = Book.objects.all()
print(book_queryset[1]) # Queries the database
print(book_queryset[1]) # Queries the database again
``` 
#### If the entire queryset has already been evaluated, the cache will be checked instead:
```python
book_queryset = Book.objects.all()
[b.title for b in book_queryset] # Queries the database
print(book_queryset[1]) # Uses cache
print(book_queryset[1]) # Uses cache
``` 
### 5. Deleting objects
```python
author1.delete() 
Author.objects.filter(age__lt=20).delete()
Authors.objects.all().delete()

# When Django deletes an object, by default it
# emulates the behavior of the SQL constraint ON DELETE CASCADE – in other words, any objects which had foreign keys pointing at the object to be deleted will be deleted along with it
``` 
### 6. Updating multiple objects at once
```python
Author.objects.filter(age__lt=20).update(age=40)

# Method update doesn’t run any save() methods on your models, or emit the
# pre_save or post_save signals (which are a consequence of calling save()),
# or honor the auto_now field option.

from django.db.models import F
Author.objects.all().update(age=F("age") + 1)
``` 
### 7. Annotation and [Aggregation]("https://docs.djangoproject.com/en/3.2/topics/db/aggregation/")
```python
from django.db.models import Count
q = Book.objects.annotate(Count("authors"))
q[0].title
>>> 'Title'
q[0].authors__count
>>> 2

from django.db.models import Avg
# Add 'average' for all authors
Author.objects.annotate(average=Avg("book__page_count"))
>>> <QuerySet [<Author: qwrd kjdfv>, <Author: kjb kjjbk>, <Author: wfew vveve>, <Author: jbl dfv>]>

# Group by "age"
Author.objects.values("age").annotate(average=Avg("book__page_count"))
>>> <QuerySet [{'age': 21, 'average': None}, {'age': 23, 'average': 12.0}, {'age': 56, 'average': 12.0}]>

# Annotate all queryset, but take only two fields
Author.objects.annotate(average=Avg("book__page_count")).values("age", "average")
>>> <QuerySet [{'age': 23, 'average': 12.0}, {'age': 56, 'average': None}, {'age': 21, 'average': None}, {'age': 56, 'average': 12.0}]>

# Aggregate annotation
from django.db.models import Avg, Count
Book.objects.annotate(num_authors=Count('authors')).aggregate(Avg('num_authors'))
>>> {'num_authors__avg': 2.0}
``` 

### 8. Select related
##### select_related works by creating an SQL join and including the fields of the related object in the SELECT statement. 
##### For this reason, select_related gets the related objects in the same database query. However, to avoid the much larger result set that would result from joining across a ‘many’ relationship, select_related is limited to single-valued relationships - foreign key and one-to-one.
```python
# Hits the database.
book = Book.objects.get(id=1)

# Hits the database again to get the related Blog object.
author = book.author # (Foreign key)

# or 

# Hits the database.
book = Book.objects.select_related('author').get(id=5)

# Doesn't hit the database, because e.blog has been prepopulated
# in the previous query.
author = book.author # (Foreign key)
```
### 9. Prefetch related
##### prefetch_related does a separate lookup for each relationship, and does the ‘joining’ in Python. 
##### This allows it to prefetch many-to-many and many-to-one objects, which cannot be done using select_related, in addition to the foreign key and one-to-one relationships that are supported by select_related.
```python
Book.objects.prefetch_related('authors')
```
### 10. [Managers]("https://docs.djangoproject.com/en/3.2/topics/db/managers/")


## НаПочитать
1. https://docs.djangoproject.com/en/3.2/topics/db/aggregation/
2. https://docs.djangoproject.com/en/3.2/howto/custom-lookups/
3. https://docs.djangoproject.com/en/3.2/ref/models/lookups/
4. https://docs.djangoproject.com/en/4.0/topics/db/managers/
5. https://docs.djangoproject.com/en/4.0/ref/models/querysets/
