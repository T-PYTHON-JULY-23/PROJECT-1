# Student Exam Management System

The Student Exam Management System is a command-line application that allows teachers and students to manage exams, grades, and student information.

## Features

- **Student Interface**: Students can view their profiles, exam grades, and take exams assigned by their teachers.
- **Teacher Interface**: Teachers can add students, assign exams, edit grades, and manage exams and questions.
- **Exam Management**: Teachers can create exams and add questions to them.
- **Grade Assignment**: Teachers can assign grades to students' exams.
- **Data Storage**: Data is stored in JSON files for easy management.

## Usage

1. **Student Interface**:

   - Students should choose the "student" option on startup.
   - They need to enter their registered student name.
   - Students will be prompted for their password.
   - After authentication, students can:
     - View their profile information.
     - View their exam grades.
     - Then if they have exams not done yet they can take exams assigned by there teachers.

2. **Teacher Interface**:

   - Teachers should choose the "teacher" option on startup.
   - They need to enter their teacher code for authentication.
   - Once authenticated, teachers can:
     - Add students and their information.
     - Assign exams to students.
     - Edit grades for students.
     - View students' information and grades.
     - Create exams and add questions to them.
     - Delete questions from exams.

3. **Taking Exams**:

   - Students can take exams that have been assigned to them by teachers.
   - They will be presented with questions and choices.
   - Students need to provide their answers by choosing the corresponding option number.
   - The system will calculate the score and assign a grade to the exam.

4. **Exam Management** (Teachers):

   - Teachers can create new exams by adding exam names.
   - They can add questions to exams and specify correct answers and choices.
   - Teachers can also delete questions from exams.

5. **Grade Assignment** (Teachers):

   - Teachers can assign grades to students' exams.
   - They can edit existing grades as needed.

6. **Data Storage**:

   - Student and teacher information, exam details, and grades are stored in JSON files.
   - Data is saved and loaded automatically as you use the application.

7. **Exiting the Program**:
   - You can exit the program at any time by selecting the "0" option.
   - The program will terminate gracefully.

Feel free to explore the features of the Student Exam Management System and make the most of its capabilities

<!-- # PROJECT-1

## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use lists or dictionaries or tuples.
- Use loops.
- Use functions that return an output .
- Use a Lambda function.
- Use at least 1 Class.
- Use some form of Error Handling .
- Organize Your Code into modules & (or packages)

## Example Project :  An online Grocery Store :

#### Overview : An online store that sells fruits to customers. This online store has 2 main users. The customer and the manager of the store . Each one of them should be able to do the following tasks for the store to function properly .

#### As a customer I should be able to do the following :
- Browse  Products .
- View the product info (summary, specs, price, quantity , etc.)
- Search for Products.
- Get recommendations for my next purchase based on my purchase history.
- Add Products to the shopping cart .
- Remove a product from the shopping cart.
- List the products in my shopping cart.
- Continue to checkout .
- Fill in my address for delivery.
- Get receipt of my purchases.
- Check delivery status .



#### Usage :
 Explain to the user how to use your project .
 for example:
 - type in search product_name to search for a product.
 - type in list_products to show all the products in the grocery.
 - type in show product_name to get information about this product.
 - type in buy product_name to buy the product .
 - and so on...


### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage.  -->
