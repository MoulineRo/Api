# BooksApi

All URIs are relative to *https://craftapi-d7d0310369b0.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createbook**](BooksApi.md#createbook) | **POST** /books | Method for add new book
[**deletebookbyid**](BooksApi.md#deletebookbyid) | **DELETE** /books/{id} | Method for delete book by id
[**getallbooks**](BooksApi.md#getallbooks) | **GET** /books | Method for get list of books
[**getbookbyid**](BooksApi.md#getbookbyid) | **GET** /books/{id} | Method for get book by id
[**updatebookbyid**](BooksApi.md#updatebookbyid) | **PUT** /books/{id} | Method for update book by id


<a name="createbook"></a>
# **createbook**
> Book createbook(book)

Method for add new book

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://craftapi-d7d0310369b0.herokuapp.com");

    BooksApi apiInstance = new BooksApi(defaultClient);
    Book book = new Book(); // Book | 
    try {
      Book result = apiInstance.createbook(book);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BooksApi#createbook");
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
 **book** | [**Book**](Book.md)|  |

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful created book |  -  |
**400** | missing name field |  -  |

<a name="deletebookbyid"></a>
# **deletebookbyid**
> List&lt;Book&gt; deletebookbyid(id)

Method for delete book by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://craftapi-d7d0310369b0.herokuapp.com");

    BooksApi apiInstance = new BooksApi(defaultClient);
    Integer id = 2; // Integer | book`s id
    try {
      List<Book> result = apiInstance.deletebookbyid(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BooksApi#deletebookbyid");
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
 **id** | **Integer**| book&#x60;s id |

### Return type

[**List&lt;Book&gt;**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful deleted book by id |  -  |
**404** | not found |  -  |

<a name="getallbooks"></a>
# **getallbooks**
> List&lt;Book&gt; getallbooks()

Method for get list of books

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://craftapi-d7d0310369b0.herokuapp.com");

    BooksApi apiInstance = new BooksApi(defaultClient);
    try {
      List<Book> result = apiInstance.getallbooks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BooksApi#getallbooks");
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

[**List&lt;Book&gt;**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful list of books |  -  |

<a name="getbookbyid"></a>
# **getbookbyid**
> Book getbookbyid(id)

Method for get book by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://craftapi-d7d0310369b0.herokuapp.com");

    BooksApi apiInstance = new BooksApi(defaultClient);
    Integer id = 2; // Integer | book`s id
    try {
      Book result = apiInstance.getbookbyid(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BooksApi#getbookbyid");
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
 **id** | **Integer**| book&#x60;s id |

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful book by id |  -  |
**404** | not found |  -  |

<a name="updatebookbyid"></a>
# **updatebookbyid**
> Book updatebookbyid(id)

Method for update book by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://craftapi-d7d0310369b0.herokuapp.com");

    BooksApi apiInstance = new BooksApi(defaultClient);
    Integer id = 2; // Integer | book`s id
    try {
      Book result = apiInstance.updatebookbyid(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BooksApi#updatebookbyid");
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
 **id** | **Integer**| book&#x60;s id |

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful updated book by id |  -  |
**400** | missing name field |  -  |

