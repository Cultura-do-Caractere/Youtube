package main

import (
	"github.com/labstack/echo/v4"
)

func main() {

	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		// return c.String(http.StatusOK, "Hello, World!")
		return c.JSON(200, map[string]interface{}{"content": "Hello, i was deployed using FluxCD"})
	})

	e.Logger.Fatal(e.Start(":1323"))

}
