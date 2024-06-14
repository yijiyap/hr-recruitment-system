import type { IPublicClientApplication} from "@azure/msal-browser";
import { PublicClientApplication } from "@azure/msal-browser";

export class PublicClientApplicationSingleton {
    private static _instance: IPublicClientApplication;
    public static create(configuration: Configuration) {
        if (PublicClientApplicationSingleton._instance ==null) {
            PublicClientApplicationSingleton._instance = new PublicClientApplication(configuration);
        }
    return PublicClientApplicationSingleton._instance;
    }
}