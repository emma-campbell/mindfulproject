import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000',
  withCredentials: false,
  headers : {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  },
  timeout: 1000,
});

export default class ApiService {

  /**
   * Return all users
   * @param perPage number of users per page
   * @param page page number
   */
  public static async getUsers(perPage: number, page: number): Promise<any> {
    return apiClient.get('/users?_limit=' + perPage + '&_page' + page);
  }

  /**
   * Return the user with the given id
   * @param id
   */
  public static async getUser(id: number): Promise<any> {
    return apiClient.get('/users/' + id);
  }

  /**
   * Create a new user given the credentials
   * @param credentials name, email, password.
   */
  public static async registerUser(credentials: object): Promise<any> {
    return apiClient.post('/users', credentials);
  }

  /**
   * Send a login request to the api
   * @param credentials email, password
   */
  public static async loginUser(credentials: object): Promise<any> {
    return apiClient.post('/login', credentials);
  }


}

