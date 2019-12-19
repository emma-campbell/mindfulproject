export default class Validator {
  public static isValidName(str: string): boolean {
    return (str.length > 3);
  }
}
