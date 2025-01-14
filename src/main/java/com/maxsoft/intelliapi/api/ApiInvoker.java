package com.maxsoft.intelliapi.api;

import com.maxsoft.intelliapi.util.FrameworkUtil;
import com.maxsoft.intelliapi.BodyType;
import com.maxsoft.intelliapi.HttpMethod;
import io.restassured.http.Headers;

import java.security.InvalidParameterException;

import static com.maxsoft.intelliapi.api.ApiRequestPayloadProcessor.getApiEndpointToBeInvoked;
import static com.maxsoft.intelliapi.api.FormDataRequestProcessor.*;
import static com.maxsoft.intelliapi.api.JsonRequestProcessor.*;
import static com.maxsoft.intelliapi.BodyType.JSON;
import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/11/2020
 * Time            : 6:56 PM
 * Description     :
 **/

public class ApiInvoker extends FrameworkUtil {

    public static void invoke(String jsonPayload, Headers headers) {
        String invokingEndpoint = getApiEndpointToBeInvoked();
        String accessTokenInFile = readAccessToken();
        String accessToken, isAuthenticationRequired, isAccessTokenRetrievedFromTextFile, accessTokenString;

        try {
            isAuthenticationRequired = getSavedValueForScenario(IS_AUTHENTICATION_REQUIRED).toLowerCase();
            isAccessTokenRetrievedFromTextFile = getSavedValueForScenario(RETRIEVE_TOKEN_FROM_TEXT_FILE).toLowerCase();
            accessTokenString = getSavedValueForScenario(MANUAL_TOKEN);
        } catch (Exception ex) {
            isAuthenticationRequired = "";
            isAccessTokenRetrievedFromTextFile = "";
            accessTokenString = "";
        }

        if (isTrue(isAuthenticationRequired)) {
            if (isTrue(isAccessTokenRetrievedFromTextFile)) {
                accessToken = accessTokenInFile;
            } else {
                accessToken = accessTokenString;
            }
        } else {
            accessToken = "";
        }

        HttpMethod httpMethod = HttpMethod.valueOf(getSavedValueForScenario(VAR_API_HTTP_METHOD).toUpperCase());

        String bodyTypeFromExcel = getSavedValueForScenario(VAR_API_REQUEST_BODY_TYPE);

        if (bodyTypeFromExcel.equals("")) {
            bodyTypeFromExcel = String.valueOf(JSON);
        }

        BodyType bodyType = BodyType.valueOf(bodyTypeFromExcel.toUpperCase());

        switch ((bodyType)) {

            case JSON:
                switch (httpMethod) {
                    case GET:
                        getApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, headers);
                        break;
                    case POST:
                        postApiWithAuthMultipleHeaders(invokingEndpoint, jsonPayload, accessToken, headers);
                        break;
                    case PUT:
                        putApiWithAuthMultipleHeaders(invokingEndpoint, jsonPayload, accessToken, headers);
                    case PATCH:
                        patchApiWithAuthMultipleHeaders(invokingEndpoint, jsonPayload, accessToken, headers);
                        break;
                    case DELETE:
                        deleteApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, headers);
                        break;
                    default:
                        throw new InvalidParameterException("HTTP Method is not implemented");
                }
                break;

            case FORM_DATA:
                switch (httpMethod) {
                    case GET:
                        getApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, headers);
                        break;
                    case POST:
                        postFormDataApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, headers);
                        break;
                    case PUT:
                        putFormDataApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, headers);
                    case PATCH:
                        patchFormDataApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, headers);
                        break;
                    case DELETE:
                        deleteApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, headers);
                        break;
                    default:
                        throw new InvalidParameterException("HTTP Method is not implemented");
                }
                break;

            default:
                throw new InvalidParameterException("Body Type is not implemented");
        }
    }
}
