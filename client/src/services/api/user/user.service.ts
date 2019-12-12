import axios from 'axios';
export const userService = {
  login
};

function login(email: string, password: string): void {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-type': 'application/json'},
    body: JSON.stringify({email, password})
  }
}
