# Advisor Admin

## Course

The first thing that you'll want to create are Courses. Courses have basic information, like the courses' name, the department, the department's abbreviation, and the course number, along with the number of credits. They also have prerequisites and corequisites. These are key, and are the information that drive the entire program, so make sure that these are correct.

## CourseCollection

Once you have a number of courses created, you can put them in CourseCollections. These form the basis of Programs, which we'll create next. Course collections have a number of courses, and then a number identify how many of those courses are required. If you're representing the core of a major, and there are 15 classes, then there this number would be 15. Were this instead a collection for senior electives, then there might be 18 classes, with three required.

## Program

Now finally, it's time to put the course collections together in Programs. The first programs you'll want to create will represent gen-eds. You'll need to create Programs for BA, BS, and Honors gen ed requirements. (Each section of the gen ed requirement will be a CourseCollection.) Set the programType to "Gen-ed" for Gen-eds or BA or BS as applicable. Once you have this, you'll be all set. The other needed information will be supplied by the user from the front end of the website.

## Student

You may however want to create some sample students, or manage students' data. Enter the student's name, select Courses they've already taken. The "Trajectory" field-- this represents student's selected paths to graduation as we'll cover below-- is optional.

## Trajectory

Trajectories are the student-created representations of their future schedules. Each 'trajectory' represents a semester that the student has created, identified with a name, so that multiple trajectories can be created and compared, and a number, indicating how many semesters in the future that trajectory represents.
