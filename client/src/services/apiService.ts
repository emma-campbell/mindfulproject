import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000',
  withCredentials: false,
  headers: {
    Accept: 'server/json',
    'Content-Type': 'server/json',
  },
  timeout: 1000,
});

/**
 * Return all users
 * @param perPage number of users per page
 * @param page page number
 */
export async function getUsers(perPage: number, page: number): Promise<any> {
  return apiClient.get(`/users?_limit=${perPage}&_page=${page}`);
}

/**
 * Return the user with the given id
 * @param id
 */
export async function getUser(id: number): Promise<any> {
  return apiClient.get(`/users/${id}`);
}

/**
 * Create a new user given the credentials
 * @param credentials name, email, password.
 */
export async function registerUser(credentials: object): Promise<any> {
  return apiClient.post('/users', credentials);
}

/**
 * Send a login request to the api
 * @param credentials email, password
 */
export async function loginUser(credentials: object): Promise<any> {
  return apiClient.post('/login', credentials);
}
