// Daily Challenge(30 minutes)
// Create a simple inventory management system using objects and arrays
const inventory = (student_name, student_id, books = []) => {
    return {
        student_name: student_name,
        student_id: student_id,
        books: books,
        student_info: {},

        // Method to add books 
        addBooks: function(bookName) {
            if (this.books.length < 5 && this.books.length > 0) {
                this.books.push(bookName)
            } else {
                console.log("You can only borrow up to 5 books a month");
            }
        },
        
        // Method to add student info
        studentInfo: function() {
            this.student_info[this.student_id] = [this.student_name, this.books];
            console.log(this.student_info);
        }
    };
}

const inventory_one = inventory("Jack", 1, ["Python Basic"]);
inventory_one.addBooks("JavaScript for begineer");
inventory_one.addBooks("JavaScript for begineer");
inventory_one.addBooks("JavaScript for begineer");
inventory_one.addBooks("JavaScript for begineer");
inventory_one.addBooks("JavaScript for begineer");
inventory_one.studentInfo();