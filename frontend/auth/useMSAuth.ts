import { BrowserCacheLocation, EventType, PublicClientApplication } from "@azure/msal-browser";
import * as msal from "@azure/msal-browser";
let tokenExpirationTimer: any;

export const useMSAuth = () => {

    const config = useRuntimeConfig();

    const msalConfig = {
        auth: {
            clientId: config.public.clientId,
            authority: config.public.authority,
        }
    };

    const msalInstance = new PublicClientApplication(msalConfig);

    async function initialize() {
        await msalInstance.initialize();

        // Handle redirect promise after login or redirect
        await msalInstance
            .handleRedirectPromise() // Handles redirect promise and obtains response
            .then((tokenResponse) => {
                if (tokenResponse !== null) {
                    // Redirect to home page after login

                } else {
                    // Redirect to error page

                }
            })
            .catch((error) => {
                // Redirect to error page
                console.error(error);
            });

        // Add event callback for login success
        msalInstance.addEventCallback((event) => {
            if (event.eventType === EventType.LOGIN_SUCCESS) {
                // set up token expiration timer

            }
        });
    }

    return {
        initialize,
    }
}