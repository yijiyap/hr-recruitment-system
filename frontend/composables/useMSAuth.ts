import { BrowserCacheLocation, EventType, PublicClientApplication } from "@azure/msal-browser";
import * as msal from "@azure/msal-browser";

let tokenExpirationTimer: any;

export const useMSAuth = () => {
    const config = useRuntimeConfig();
    const msalConfig = {
        auth: {
            clientId: config.public.clientId,
            authority: config.public.authority,
            redirectUri: config.public.redirectUri,
            postLogoutRedirectUri: config.public.postLogoutRedirectUri,
            navigateToLoginRequestUrl: true,
        },
        cache: {
            cacheLocation: BrowserCacheLocation.LocalStorage,
            storeAuthStateInCookie: true,
        }
    };

    let msalInstance = new PublicClientApplication(msalConfig);
    console.log("MSAL instance created", msalInstance);

    // Initialize MSAL instance
    async function initialize() {
        await msalInstance.initialize();

        await msalInstance.handleRedirectPromise().then((response) => { // check for redirect response
                if (response) {
                    handleResponse(response);
                }
            }).catch(error => {
                console.log(error);
            })
        

        msalInstance.addEventCallback((event) => {
            if (event.eventType === EventType.LOGIN_SUCCESS) { // handle login success event
                setupTokenExpirationTimer();
            }
        });
    }

    // Handle response from redirect
    function handleResponse(response: any) {
        if (response?.account) {
            setupTokenExpirationTimer();
        } else {
            console.log("huh?");
        }
    }

    // Set up timer for refreshing access token upon expiration
    function setupTokenExpirationTimer() { 
        const accounts = msalInstance.getAllAccounts();
        if (accounts.length > 0) {
            const account = accounts[0]; // if multiple accounts are supported, this should be handled differently
            if (account.idTokenClaims && account.idTokenClaims.exp) { // check if token has expiration time
                const tokenExpirationTime = account.idTokenClaims.exp * 1000;
                const currentTime = Date.now()
                const timeUntilExpiration = tokenExpirationTime - currentTime;

                clearTimeout(tokenExpirationTimer); // clear existing timer if it exists

                tokenExpirationTimer = setTimeout(() => { // set new timer
                    refreshAccessToken(account);
                }, timeUntilExpiration)
            }
        }
    }

    // Refresh access token
    async function refreshAccessToken(account: any) {
        try {
            const response = await msalInstance.acquireTokenSilent({
                account: account,
                scopes: ["User.Read"],
            });
            console.log("Access token refreshed", response.accessToken);
            setupTokenExpirationTimer();
        } catch (error) {
            console.log("Error refreshing access token", error);
            // sign out maybe?
        } 
    }

    // sign in with redirect
    async function signIn() {
        try {
            await msalInstance.loginRedirect(
                {
                    scopes: ["User.Read"],
                }
            );
        } catch (error) {
            console.error("Error signing in", error);
        }
    }

    // acquire access token silently. This is used to authenticate requests to the API
    async function acquireTokenSilent() {
        const accounts = msalInstance.getAllAccounts();
        if (accounts.length > 0) {
            const account = accounts[0]; // if multiple accounts are supported, this should be handled differently
            msalInstance.setActiveAccount(account); // set active account
            try {
                const response = await msalInstance.acquireTokenSilent({ // silent because we are not prompting the user
                    account: account,
                    scopes: ["User.Read"],
                });
                return response.accessToken;
            } catch (error) {
                console.log("Error acquiring token silently", error);
                return null;
            }
        } else {
            console.log("No accounts found");
            return null;
        }
    }

    // Get all MSAL accounts
    function getAccounts() {
        return msalInstance.getAllAccounts();
    }

    // Check if user is authenticated
    function isAuthenticated() {
        return getAccounts().length > 0;
    }

    // Sign out
    function signOut(accountId: string) {
        const account = accountId ? msalInstance.getAccountByHomeId(accountId) : null;

        if (account) {
            msalInstance.logoutRedirect({account: account});
            localStorage.clear();
        } else {
            console.log("No account found")
        }
    }

    return {
        initialize,
        msalInstance,
        signIn,
        getAccounts,
        acquireTokenSilent,
        isAuthenticated,
        signOut,
    }
}