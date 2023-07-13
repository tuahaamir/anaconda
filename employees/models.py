from django.db import models
from datetime import datetime
from django.utils import timezone

class Skills(models.Model):
    skill_name = models.CharField(max_length=32)
    skill_type = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        db_table = "skills"

class Employee(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=12)
    department_id = models.BigIntegerField(blank=True)
    department = models.CharField(max_length=50, blank=True)
    start_time = models.TimeField(auto_now_add=True)
    leaves = models.IntegerField(default=18)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skills, through='EmployeeSkills', related_name='employees', blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        db_table = "employees"
        
# Custom employees_skills Table columns
class EmployeeSkills(models.Model):
    employee = models.ForeignKey(Employee, db_column='employee_id', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, db_column='skill_id', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "employee_skills"
        
class EmployeeDetails(models.Model):
    JOB_STATUS_CHOICES = [
        ("intern", "Internee"),
        ("irobation", "Probation Period"),
        ("onboard", "Onboard"),
        ("notice", "Notice Period"),
    ]
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)
    date_of_birth = models.DateField(blank=True)
    cnic = (models.CharField(blank=True, max_length=16))
    joining_date = models.DateField(blank=True)
    contact_number = models.CharField(max_length=12)
    salary = models.IntegerField()
    job_status = models.CharField(max_length=32, choices=JOB_STATUS_CHOICES)
    role = models.CharField(max_length=50, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    bank_name = models.CharField(blank=True)
    bank_account_number = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.employee.first_name + ' ' + self.employee.last_name
    
    class Meta:
        db_table = "employee_details"
        
        
    
"""
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    checkedin_at = models.DateTimeField(default=timezone.localtime(), null=True, blank=True)
    checkedout_at = models.DateTimeField(default=timezone.localtime(), null=True, blank=True)
    day = models.CharField(default=datetime.now().date().strftime('%w'))
    month = models.CharField(default=datetime.now().month)
    year = models.CharField(default=datetime.now().year)
    
    
    def __str__(self) -> str:
        return self.employee.first_name + " " + str(self.checkedin_at.day)+'-'+str(self.checkedin_at.month)+'-'+str(self.checkedin_at.year)
    
"""

class EmployeeFinance(models.Model):
    salary = models.IntegerField(null=True, blank=True)
    provident = models.FloatField(default=2.5)
    fuel_allowance = models.IntegerField(default=3000)
    special_allowance = models.IntegerField(default=0)
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.employee.first_name
    
    
class Holiday(models.Model):
    holiday_title = models.CharField(max_length=30)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.holiday_title
    
    class Meta:
        db_table = "holidays"
        
        
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    check_in = models.TimeField()
    check_out = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.employee.first_name + " " + self.employee.last_name
    
    class Meta:
        db_table = "check_ins"
        