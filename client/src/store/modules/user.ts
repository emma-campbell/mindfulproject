import {
  VuexModule, Module, Action, Mutation, getModule,
} from 'vuex-module-decorators';
import { loginUser } from '@/services/apiService';
import { getToken, setToken, removeToken } from '@/utils/cookies';
import router from '@/router';
import store from '@/store';

export interface IUserState {
  token: string,
  id: number | undefined,
  name: string,
  email: string,
}

@Module({ dynamic: true, store, name: 'user' })
class User extends VuexModule implements IUserState {
  public token = getToken() || '';

  public id = undefined;

  public name = '';

  public email = '';

  @Mutation
  private set_id(id: any) {
    this.id = id;
  }

  @Mutation
  private set_token(token: string) {
    this.token = token;
  }

  @Mutation
  private set_name(name: string) {
    this.name = name;
  }

  @Mutation
  private set_email(email: string) {
    this.email = email;
  }

  @Action
  public async Login(userInfo: { email: string, password: string}) {
    let { email, password } = userInfo;
    email = email.trim();

    // send the request to the server
    const { data } = await loginUser({ email, password });

    // add the token to cookies and set the token in vuex
    setToken(data.access_token);
    this.set_token(data.access_token);

    // store the user info
    this.set_id(data.user.id);
    this.set_name(data.user.name);
    this.set_email(data.user.email);
  }

  @Action
  public resetToken() {
    removeToken();
    this.set_token('');
  }

  @Action
  public async getUserInfo() {
    if (this.token === '') {
      throw Error('getUserInfo: token is undefined!');
    }
    // @ts-ignore
    const { data } = await ApiService.getUser(this.id);
    if (!data) throw Error('Verification failed, please login again.');
    const { name, email, id } = data.user;
    this.set_email(email);
    this.set_name(name);
    this.set_id(id);
  }
}
