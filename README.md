Python Junior Task

Create a REST API for cars. It should contain accounts, CarBrand, UserCar, and CarModels. Each user has to be extended by default Django abstract class and should contain a few more columns (for your choice). Each car object contains relations to the user and CarBrand. Each CarModel contains relation to CarBrand. It is all your decision how you will distribute models to different apps. Please make the API URLs with filters (custom typed). All models should be with soft delete.

Models fields:
CarBrand [name, created_at, deleted_at]
CarModel [car_brand, name, created_at, update_at]
UserCar [user, car_brand, car_model, first_reg, odometer, created_at, deleted_at]

Auth:
Please extend the default Django user class and add some custom fields. Create login, and register functionality. User default Django permission classes. 

