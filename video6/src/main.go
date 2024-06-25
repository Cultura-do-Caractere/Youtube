package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func main() {

	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		// return c.String(http.StatusOK, "Hello, World!")
		return c.JSON(200, map[string]interface{}{"name": "data"})
	})
	e.GET("/groups", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})

	e.GET("/users", func(c echo.Context) error {
		response := map[string]interface{}{
			"name":      "user 1",
			"id":        1,
			"validated": true}
		return c.JSON(200, response)
	})
	e.Logger.Fatal(e.Start(":1323"))

}
