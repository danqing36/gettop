# Created by fq at 11/29/21
Feature: Test Scenarios for check gettop all products sort page
  # Enter feature description here

  Scenario Outline: Check gettop website all categories sort links
    Given Open gettop page
    When Click on <category> category
     And Select sort method <sort_method>
    Then verify macbook product <sort_method>
    Examples:
    |category   | sort_method                |
    |mac        | Sort by price: low to high |
    |mac        | Sort by price: high to low |
    |iphone     | Sort by price: low to high |
    |iphone     | Sort by price: high to low |
    |ipad       | Sort by price: low to high |
    |ipad       | Sort by price: high to low |
    |watch      | Sort by price: low to high |
    |watch      | Sort by price: high to low |
    |accessories    | Sort by price: low to high |
    |accessories    | Sort by price: high to low |


