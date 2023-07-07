/*
 * Books API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Author;
import org.openapitools.client.model.Error;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AuthorsApi
 */
@Ignore
public class AuthorsApiTest {

    private final AuthorsApi api = new AuthorsApi();

    
    /**
     * Method for get all authors
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getallauthorsTest() throws ApiException {
        List<Author> response = api.getallauthors();

        // TODO: test validations
    }
    
    /**
     * Method for get author by id
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getauthorbyidTest() throws ApiException {
        Integer id = null;
        Author response = api.getauthorbyid(id);

        // TODO: test validations
    }
    
}