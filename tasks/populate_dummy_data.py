# Create a file named populate_dummy_data.py in your app directory

from django.utils import timezone
from django.contrib.auth.models import User
import random
from datetime import timedelta
from .models import Project, Task

def create_dummy_data():
    # Check if we already have some data
    if Project.objects.count() > 0:
        print("Data already exists. Skipping dummy data creation.")
        return
    
    # Create a test user if none exists
    if User.objects.count() == 0:
        test_user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='password123'
        )
    else:
        test_user = User.objects.first()
    
    # Create dummy projects
    project_data = [
        {
            'name': 'Web Application Redesign',
            'description': 'Completely overhaul the user interface and improve user experience for our main web application.'
        },
        {
            'name': 'Mobile App Development',
            'description': 'Create native mobile applications for iOS and Android platforms to expand our market reach.'
        },
        {
            'name': 'Data Migration Project',
            'description': 'Transition from legacy database systems to our new cloud-based solution with minimal downtime.'
        },
        {
            'name': 'Marketing Campaign',
            'description': 'Develop and execute a comprehensive marketing strategy for Q4 product launch.'
        },
        {
            'name': 'Research and Development',
            'description': 'Explore new technologies and methodologies to keep our product competitive in the market.'
        },
        {
            'name': 'Internal Tools',
            'description': 'Build custom tools to improve team productivity and streamline internal processes.'
        },
        {
            'name': 'Customer Portal Update',
            'description': 'Enhance the customer portal with new features and improved security measures.'
        }
    ]
    
    created_projects = []
    for project in project_data:
        created_project = Project.objects.create(
            name=project['name'],
            description=project['description']
        )
        created_projects.append(created_project)
        print(f"Created project: {created_project.name}")
    
    # Create dummy tasks with random assignments
    task_titles = [
        'Initial planning', 'Requirements gathering', 'Design mockups',
        'Backend development', 'Frontend implementation', 'Database setup',
        'API integration', 'Security review', 'Performance testing',
        'Bug fixes', 'Documentation', 'Client presentation',
        'Team training', 'Deployment preparation', 'Launch coordination',
        'Post-launch monitoring', 'Feedback collection', 'Analytics setup',
        'Backup system configuration', 'User acceptance testing'
    ]
    
    task_descriptions = [
        'Define project scope, goals, and deliverables with all stakeholders.',
        'Gather and document detailed requirements from all departments involved.',
        'Create visual designs and prototypes for approval.',
        'Implement server-side logic and data structures.',
        'Develop the user interface components and client-side functionality.',
        'Configure and optimize database schema and performance.',
        'Connect with third-party services and ensure smooth data flow.',
        'Perform thorough security audit and address vulnerabilities.',
        'Identify and resolve performance bottlenecks.',
        'Address reported issues and improve functionality.',
        'Create comprehensive documentation for developers and end-users.',
        'Present progress and results to clients or management.',
        'Conduct training sessions for team members on new technologies.',
        'Prepare servers, environments, and deployment scripts.',
        'Coordinate all aspects of the product launch across teams.',
        'Monitor system performance and user behavior after release.',
        'Collect and analyze user feedback for future improvements.',
        'Set up tracking and reporting for key performance indicators.',
        'Ensure reliable backup and recovery systems are in place.',
        'Validate that the solution meets all acceptance criteria.'
    ]
    
    priorities = ['Low', 'Medium', 'High']
    statuses = ['Pending', 'In Progress', 'Completed']
    
    today = timezone.now().date()
    
    # Create 3-5 tasks for each project
    for project in created_projects:
        num_tasks = random.randint(3, 5)
        
        # Get random but not repeating task titles for this project
        project_task_titles = random.sample(task_titles, num_tasks)
        project_task_descriptions = random.sample(task_descriptions, num_tasks)
        
        for i in range(num_tasks):
            # Generate a random due date between today and 30 days from now
            due_date = today + timedelta(days=random.randint(1, 30))
            
            Task.objects.create(
                title=project_task_titles[i],
                description=project_task_descriptions[i],
                due_date=due_date,
                priority=random.choice(priorities),
                status=random.choice(statuses),
                project=project,
                user=test_user
            )
            print(f"Created task: {project_task_titles[i]} for project {project.name}")
    
    print("Dummy data creation completed successfully!")

# You can run this function directly using the shell or create a management command