# AuthorsApi

All URIs are relative to *https://craftapi-d7d0310369b0.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getallauthors**](AuthorsApi.md#getallauthors) | **GET** /authors | Method for get all authors
[**getauthorbyid**](AuthorsApi.md#getauthorbyid) | **GET** /authors/{id} | Method for get author by id


<a name="getallauthors"></a>
# **getallauthors**
> List&lt;Author&gt; getallauthors()

Method for get all authors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://craftapi-d7d0310369b0.herokuapp.com");

    AuthorsApi apiInstance = new AuthorsApi(defaultClient);
    try {
      List<Author> result = apiInstance.getallauthors();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorsApi#getallauthors");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Author&gt;**](Author.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful list of authors |  -  |

<a name="getauthorbyid"></a>
# **getauthorbyid**
> Author getauthorbyid(id)

Method for get author by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://craftapi-d7d0310369b0.herokuapp.com");

    AuthorsApi apiInstance = new AuthorsApi(defaultClient);
    Integer id = 2; // Integer | author`s id
    try {
      Author result = apiInstance.getauthorbyid(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorsApi#getauthorbyid");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| author&#x60;s id |

### Return type

[**Author**](Author.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful author by id |  -  |
**404** | not found |  -  |

