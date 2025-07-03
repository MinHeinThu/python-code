// Create a student management system
const createStudent = (name, age, courses = []) => {
    return {
        name: name,
        age: age,
        courses: courses,
        grades: {},
        
        // Method to add a course
        addCourse: function(courseName) {
            if (!this.courses.includes(courseName)) {
                this.courses.push(courseName);
            }
        },
        
        // Method to add a grade
        addGrade: function(course, grade) {
            this.grades[course] = grade;
        },
        
        // Method to calculate GPA
        calculateGPA: function() {
            const grades = Object.values(this.grades);
            if (grades.length === 0) return 0;
            const sum = grades.reduce((acc, grade) => acc + grade, 0);
            return sum / grades.length;
        },
        
        // Method to get student info
        getInfo: function() {
            return `${this.name} (${this.age}) - Courses: ${this.courses.join(", ")} - GPA: ${this.calculateGPA().toFixed(2)}`;
        }
    };
};

// Test the student object
const student1 = createStudent("John", 20, ["Math", "Physics"]);
student1.addCourse("Chemistry");
student1.addGrade("Math", 85);
student1.addGrade("Physics", 92);
student1.addGrade("Chemistry", 78);
console.log(student1.getInfo());