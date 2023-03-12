import unittest
from app import app, kanban

class Kanban_Board_Test(unittest.TestCase):

    def test_add_task(self):
        with app.test_client() as client:
            response = client.post('/add_task', data=dict(
                added_task='Task 1',
                status='to do'))

            self.assertIn(b'Task 1', response.data)
    

    def test_delete_task(self):
        with app.test_client() as client:
            client.post('/add_task', data=dict(
                added_task='Task 2', 
                status='completed'))

            response = client.post('/delete_task', data=dict(
                deleted_task='Task 2', 
                status='completed'))
            self.assertNotIn(b'Task 2', response.data)
    

    def test_move_task(self):
        with app.test_client() as client:

            client.post('/add_task', data={'added_task': 'Task 3', 'status': 'to do'})
            response_1 = client.post('/move_task', data={'moving_task': 'Task 3', 'status': 'in progress'})
            self.assertEqual(response_1.status_code, 200)
            self.assertIn('Task 3', kanban['in progress'])
            response_2 = client.post("/delete_task", data={'deleted_task': 'Task 3', 'status': 'in progress'})
            self.assertEqual(response_2.status_code, 200)


    def test_move_task_2(self):
        with app.test_client() as client:
            client.post('/add_task', data={'added_task': 'Task 4', 'status': 'in progress'})
            response_2 = client.post('/move_task', data={'moving_task': 'Task 4', 'status': 'completed'})
            self.assertEqual(response_2.status_code, 200)
            self.assertIn('Task 4', kanban['completed'])
            response_3 = client.post("/delete_task", data={'deleted_task': 'Task 4', 'status': 'completed'})
            self.assertEqual(response_3.status_code, 200)


    def test_move_task_not_in_there(self):
        with app.test_client() as client:
        
            client.post('/add_task', data={'added_task': 'Task 5', 'status': 'to do'})
            response_3 = client.post('/move_task', data={'moving_task': 'Task 5', 'status': 'completed'})
            self.assertEqual(response_3.status_code, 200)
            self.assertNotIn('Imaginary Task', kanban['completed'])
    
   
    def test_register_login(self):
        with app.test_client() as client:

            client.post("/register", data=dict(
                first_name="John",
                last_name="Doe",
                email="johndoe@example.com",
                password="password123",
            ), follow_redirects=True)

            response = client.post("/login", data=dict(
                email="johndoe@example.com",
                password="password123"
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)

           
if __name__=="__main__":
    unittest.main()