/*
    Schema

    Student:
        ID
        Name
    Teacher:
        ID
        Name
    Course:
        ID
        Name
    StudentTeacherCourse:
        StudentID
        TeacherID
        CourseID
*/

-- A query to find name of students taught by teacher whose name is 'John'

Select Student.Name from Student
inner join StudentTeacherCourse on Student.ID = StudentTeacherCourse.StudentID
inner join Teacher on StudentTeacherCourse.TeacherID = Teacher.ID
where Teacher.Name = 'John'

-- alternatively

Select Student.Name from Student
where Student.ID in (
    Select StudentTeacherCourse.StudentID from StudentTeacherCourse
    where StudentTeacherCourse.TeacherID in (
        Select Teacher.ID from Teacher
        where Teacher.Name = 'John'
    )
)
