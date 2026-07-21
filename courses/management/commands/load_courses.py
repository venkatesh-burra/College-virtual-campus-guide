"""
Management command to load sample courses into the database.
Usage: python manage.py load_courses
"""
from django.core.management.base import BaseCommand
from courses.models import Course


class Command(BaseCommand):
    help = 'Load sample courses for QIS College'

    def handle(self, *args, **options):
        # Sample course data as per project requirements
        courses_data = [
            {
                'course_name': 'B.Tech - Computer Science Engineering',
                'duration': '4 Years',
                'annual_fee': 85000,
                'eligibility': '10+2 with PCM (60% marks)',
                'description': 'Learn programming, software development, AI, and data structures. Prepare for careers in IT companies and startups.',
            },
            {
                'course_name': 'B.Tech - Electronics and Communication Engineering',
                'duration': '4 Years',
                'annual_fee': 85000,
                'eligibility': '10+2 with PCM (60% marks)',
                'description': 'Study electronic circuits, communication systems, VLSI design, and embedded systems.',
            },
            {
                'course_name': 'B.Tech - Electrical Engineering',
                'duration': '4 Years',
                'annual_fee': 85000,
                'eligibility': '10+2 with PCM (60% marks)',
                'description': 'Focus on power systems, electrical machines, control systems, and renewable energy.',
            },
            {
                'course_name': 'B.Tech - Mechanical Engineering',
                'duration': '4 Years',
                'annual_fee': 85000,
                'eligibility': '10+2 with PCM (60% marks)',
                'description': 'Learn machine design, thermodynamics, manufacturing processes, and CAD/CAM.',
            },
            {
                'course_name': 'B.Tech - Civil Engineering',
                'duration': '4 Years',
                'annual_fee': 85000,
                'eligibility': '10+2 with PCM (60% marks)',
                'description': 'Study structural design, construction management, surveying, and environmental engineering.',
            },
            {
                'course_name': 'MBA',
                'duration': '2 Years',
                'annual_fee': 60000,
                'eligibility': 'Graduation in any discipline (50% marks)',
                'description': 'Master business administration with specializations in Finance, Marketing, and HR.',
            },
            {
                'course_name': 'MCA',
                'duration': '2 Years',
                'annual_fee': 55000,
                'eligibility': 'Graduation with Mathematics (50% marks)',
                'description': 'Advanced computer applications including software engineering, databases, and web technologies.',
            },
            {
                'course_name': 'M.Tech',
                'duration': '2 Years',
                'annual_fee': 50000,
                'eligibility': 'B.Tech/B.E in relevant branch (55% marks)',
                'description': 'Postgraduate engineering program with research-oriented curriculum and industry projects.',
            },
        ]

        created_count = 0
        for data in courses_data:
            course, created = Course.objects.get_or_create(
                course_name=data['course_name'],
                defaults=data,
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created: {course.course_name}')
            else:
                self.stdout.write(f'Already exists: {course.course_name}')

        self.stdout.write(self.style.SUCCESS(f'Done! {created_count} new courses added.'))
